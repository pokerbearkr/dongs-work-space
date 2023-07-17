SELECT b.title,a.board_id,b.reply_id,b.writer_id,b.contents,b.created_date
from used_goods_board a,used_goods_reply b
where to_char(a.created_date,'yyyy-dd')='2022-10' and a.board_id=b.board_id
order by a.created_date,b.title