import pymysql
import pymysql.cursors
from datetime import datetime, timedelta

host = "localhost"
user = "root"
password = "autoset"
db = "project"

def server_connection(host, user, password, db): # DB 연결
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("연결 성공")
        return connection
    except pymysql.Error as e:
        print(f"The error '{e}' occurred")
        return None

def signup(connection): # 회원 가입
    try:
        user_id = input("ID: ")
        password = input("Password: ")
        user_type = input("User type: ")
        latitude = input("latitude: ")
        longitude = input("longitude: ")

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            print("위치 입력 오류")
            return

        with connection.cursor() as cursor: # 사용자 중복 확인
            sql = "SELECT * FROM user WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            if cursor.fetchone() is not None:
                print("이미 존재하는 사용자 ID")
                return
            # 추가
            sql = """
            INSERT INTO user (user_id, password, user_type, latitude, longitude) 
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (user_id, password, user_type, latitude, longitude))
            connection.commit()
            print("User added successfully")

    except pymysql.Error as e:
        print(f"The error '{e}' occurred")
    
def make_reservation(connection, user_id, station_id, charger_id, start_datetime):
    try:
        
        start_datetime = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + timedelta(minutes=30)

        if not (start_datetime.minute in [0, 30] and start_datetime.second == 0):
            print("예약은 정각 또는 30분에만 가능합니다")
            return False

        with connection.cursor() as cursor:
            
            cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            if cursor.fetchone() is None:
                print("존재하지 않는 사용자 ID입니다.")
                return False

            
            cursor.execute(""" 
                SELECT slot_id FROM reservation_slots
                WHERE charging_station_id = %s AND charger_id = %s 
                AND start_datetime = %s AND end_datetime = %s AND status = 'reserved'
                """, (station_id, charger_id, start_datetime, end_datetime))

            existing_reservation = cursor.fetchone()
            if existing_reservation:
                manage_reservation_queue(connection, existing_reservation['slot_id'], user_id)
                print("이미 예약된 시간입니다. 대기열에 추가됩니다.")
                return False

            cursor.execute("""
                INSERT INTO reservation_slots (user_id, charging_station_id, charger_id, start_datetime, end_datetime, status)
                VALUES (%s, %s, %s, %s, %s, 'reserved')
                """, (user_id, station_id, charger_id, start_datetime, end_datetime))
            connection.commit()
            print(f"예약 완료: {start_datetime} 부터 {end_datetime}")
            return True
    except pymysql.Error as e:
        print(f"Error occurred: {e}")
        return False
    
def cancel_reservation(connection, user_id, station_id, charger_id, start_datetime):
    try:
        start_datetime = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M")

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT slot_id FROM reservation_slots
                WHERE user_id = %s AND charging_station_id = %s AND charger_id = %s 
                AND start_datetime = %s AND status = 'reserved'
                """, (user_id, station_id, charger_id, start_datetime))
            reservation = cursor.fetchone()

            if reservation is None:
                print("취소할 예약이 존재하지 않습니다")
                return False

            cursor.execute(""" 
                UPDATE reservation_slots
                SET status = 'cancelled'  # 또는 'available' 상태로 변경
                WHERE slot_id = %s
                """, (reservation['slot_id'],))
            connection.commit()

            assign_reservation_to_next_in_queue(connection, reservation['slot_id'])
            print("예약 취소 완료")
            return True
    except pymysql.Error as e:
        print(f"Error occurred: {e}")
        return False

def manage_reservation_queue(connection, slot_id, user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reservation_queue (slot_id, user_id)
                VALUES (%s, %s)
                """, (slot_id, user_id))
            connection.commit()
            print("대기자 추가 완료")
    except pymysql.Error as e:
        print(f"Error occurred: {e}")

def assign_reservation_to_next_in_queue(connection, slot_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT user_id FROM reservation_queue
                WHERE slot_id = %s
                ORDER BY queue_id ASC
                LIMIT 1
                """, (slot_id,))
            next_user = cursor.fetchone()

            if next_user:
                cursor.execute("""
                    UPDATE reservation_slots
                    SET user_id = %s, status = 'reserved'
                    WHERE slot_id = %s AND status = 'available'
                    """, (next_user['user_id'], slot_id))
                cursor.execute("""
                    DELETE FROM reservation_queue
                    WHERE user_id = %s AND slot_id = %s
                    """, (next_user['user_id'], slot_id))
                connection.commit()
                print("다음 대기자에게 예약 할당 완료")
    except pymysql.Error as e:
        print(f"Error occurred: {e}")

def main():
    connection = server_connection(host, user, password, db)
    if connection is None:
        print("서버 연결 실패")
        return
    while True:
        print("\n메뉴:")
        print("1. 회원 가입")
        print("2. 예약 생성")
        print("3. 예약 취소")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            signup(connection)
        elif choice == '2':
            user_id = input("사용자 ID: ")
            station_id = input("충전소 ID: ")
            charger_id = input("충전기 ID: ")
            start_datetime = input("예약 시작 시간 (YYYY-MM-DD HH:MM): ")
            make_reservation(connection, user_id, station_id, charger_id, start_datetime)
        elif choice == '3':
            user_id = input("사용자 ID: ")
            station_id = input("충전소 ID: ")
            charger_id = input("충전기 ID: ")
            start_datetime = input("예약 시작 시간 (YYYY-MM-DD HH:MM): ")
            cancel_reservation(connection, user_id, station_id, charger_id, start_datetime)
        elif choice == '4':
            print("프로그램 종료")
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()