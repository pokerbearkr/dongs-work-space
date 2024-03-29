-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	5.6.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sigungu`
--

DROP TABLE IF EXISTS `sigungu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sigungu` (
  `sigungu_code` int(11) NOT NULL,
  `ENG_NM` text,
  `KOR_NM` text,
  PRIMARY KEY (`sigungu_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sigungu`
--

LOCK TABLES `sigungu` WRITE;
/*!40000 ALTER TABLE `sigungu` DISABLE KEYS */;
INSERT INTO `sigungu` VALUES (11110,'Jongno-gu','종로구'),(11140,'Jung-gu','중구'),(11170,'Yongsan-gu','용산구'),(11200,'Seongdong-gu','성동구'),(11215,'Gwangjin-gu','광진구'),(11230,'Dongdaemun-gu','동대문구'),(11260,'Jungnang-gu','중랑구'),(11290,'Seongbuk-gu','성북구'),(11305,'Gangbuk-gu','강북구'),(11320,'Dobong-gu','도봉구'),(11350,'Nowon-gu','노원구'),(11380,'Eunpyeong-gu','은평구'),(11410,'Seodaemun-gu','서대문구'),(11440,'Mapo-gu','마포구'),(11470,'Yangcheon-gu','양천구'),(11500,'Gangseo-gu','강서구'),(11530,'Guro-gu','구로구'),(11545,'Geumcheon-gu','금천구'),(11560,'Yeongdeungpo-gu','영등포구'),(11590,'Dongjak-gu','동작구'),(11620,'Gwanak-gu','관악구'),(11650,'Seocho-gu','서초구'),(11680,'Gangnam-gu','강남구'),(11710,'Songpa-gu','송파구'),(11740,'Gangdong-gu','강동구'),(26110,'Jung-gu','중구'),(26140,'Seo-gu','서구'),(26170,'Dong-gu','동구'),(26200,'Yeongdo-gu','영도구'),(26230,'Busanjin-gu','부산진구'),(26260,'Dongnae-gu','동래구'),(26290,'Nam-gu','남구'),(26320,'Buk-gu','북구'),(26350,'Haeundae-gu','해운대구'),(26380,'Saha-gu','사하구'),(26410,'Geumjeong-gu','금정구'),(26440,'Gangseo-gu','강서구'),(26470,'Yeonje-gu','연제구'),(26500,'Suyeong-gu','수영구'),(26530,'Sasang-gu','사상구'),(26710,'Gijang-gun','기장군'),(27110,'Jung-gu','중구'),(27140,'Dong-gu','동구'),(27170,'Seo-gu','서구'),(27200,'Nam-gu','남구'),(27230,'Buk-gu','북구'),(27260,'Suseong-gu','수성구'),(27290,'Dalseo-gu','달서구'),(27710,'Dalseong-gun','달성군'),(27720,'Gunwi-gun','군위군'),(28110,'Jung-gu','중구'),(28140,'Dong-gu','동구'),(28177,'Michuhol-gu','미추홀구'),(28185,'Yeonsu-gu','연수구'),(28200,'Namdong-gu','남동구'),(28237,'Bupyeong-gu','부평구'),(28245,'Gyeyang-gu','계양구'),(28260,'Seo-gu','서구'),(28710,'Ganghwa-gun','강화군'),(28720,'Ongjin-gun','옹진군'),(29110,'Dong-gu','동구'),(29140,'Seo-gu','서구'),(29155,'Nam-gu','남구'),(29170,'Buk-gu','북구'),(29200,'Gwangsan-gu','광산구'),(30110,'Dong-gu','동구'),(30140,'Jung-gu','중구'),(30170,'Seo-gu','서구'),(30200,'Yuseong-gu','유성구'),(30230,'Daedeok-gu','대덕구'),(31110,'Jung-gu','중구'),(31140,'Nam-gu','남구'),(31170,'Dong-gu','동구'),(31200,'Buk-gu','북구'),(31710,'Ulju-gun','울주군'),(36110,'Sejong-si','세종특별자치시'),(41111,'Jangan-gu, Suwon-si','수원시 장안구'),(41113,'Gwonseon-gu, Suwon-si','수원시 권선구'),(41115,'Paldal-gu, Suwon-si','수원시 팔달구'),(41117,'Yeongtong-gu, Suwon-si','수원시 영통구'),(41131,'Sujeong-gu, Seongnam-si','성남시 수정구'),(41133,'Jungwon-gu, Seongnam-si','성남시 중원구'),(41135,'Bundang-gu, Seongnam-si','성남시 분당구'),(41150,'Uijeongbu-si','의정부시'),(41171,'Manan-gu, Anyang-si','안양시 만안구'),(41173,'Dongan-gu, Anyang-si','안양시 동안구'),(41190,'Bucheon-si','부천시'),(41210,'Gwangmyeong-si','광명시'),(41220,'Pyeongtaek-si','평택시'),(41250,'Dongducheon-si','동두천시'),(41271,'Sangnok-gu, Ansan-si','안산시 상록구'),(41273,'Danwon-gu, Ansan-si','안산시 단원구'),(41281,'Deogyang-gu, Goyang-si','고양시 덕양구'),(41285,'Ilsandong-gu, Goyang-si','고양시 일산동구'),(41287,'Ilsanseo-gu, Goyang-si','고양시 일산서구'),(41290,'Gwacheon-si','과천시'),(41310,'Guri-si','구리시'),(41360,'Namyangju-si','남양주시'),(41370,'Osan-si','오산시'),(41390,'Siheung-si','시흥시'),(41410,'Gunpo-si','군포시'),(41430,'Uiwang-si','의왕시'),(41450,'Hanam-si','하남시'),(41461,'Cheoin-gu, Yongin-si','용인시 처인구'),(41463,'Giheung-gu, Yongin-si','용인시 기흥구'),(41465,'Suji-gu, Yongin-si','용인시 수지구'),(41480,'Paju-si','파주시'),(41500,'Icheon-si','이천시'),(41550,'Anseong-si','안성시'),(41570,'Gimpo-si','김포시'),(41590,'Hwaseong-si','화성시'),(41610,'Gwangju-si','광주시'),(41630,'Yangju-si','양주시'),(41650,'Pocheon-si','포천시'),(41670,'Yeoju-si','여주시'),(41800,'Yeoncheon-gun','연천군'),(41820,'Gapyeong-gun','가평군'),(41830,'Yangpyeong-gun','양평군'),(43111,'Sangdang-gu, Cheongju-si','청주시 상당구'),(43112,'Seowon-gu, Cheongju-si','청주시 서원구'),(43113,'Heungdeok-gu, Cheongju-si','청주시 흥덕구'),(43114,'Cheongwon-gu, Cheongju-si','청주시 청원구'),(43130,'Chungju-si','충주시'),(43150,'Jecheon-si','제천시'),(43720,'Boeun-gun','보은군'),(43730,'Okcheon-gun','옥천군'),(43740,'Yeongdong-gun','영동군'),(43745,'Jeungpyeong-gun','증평군'),(43750,'Jincheon-gun','진천군'),(43760,'Goesan-gun','괴산군'),(43770,'Eumseong-gun','음성군'),(43800,'Danyang-gun','단양군'),(44131,'Dongnam-gu, Cheonan-si','천안시 동남구'),(44133,'Seobuk-gu, Cheonan-si','천안시 서북구'),(44150,'Gongju-si','공주시'),(44180,'Boryeong-si','보령시'),(44200,'Asan-si','아산시'),(44210,'Seosan-si','서산시'),(44230,'Nonsan-si','논산시'),(44250,'Gyeryong-si','계룡시'),(44270,'Dangjin-si','당진시'),(44710,'Geumsan-gun','금산군'),(44760,'Buyeo-gun','부여군'),(44770,'Seocheon-gun','서천군'),(44790,'Cheongyang-gun','청양군'),(44800,'Hongseong-gun','홍성군'),(44810,'Yesan-gun','예산군'),(44825,'Taean-gun','태안군'),(45111,'Wansan-gu, Jeonju-si','전주시 완산구'),(45113,'Deokjin-gu, Jeonju-si','전주시 덕진구'),(45130,'Gunsan-si','군산시'),(45140,'Iksan-si','익산시'),(45180,'Jeongeup-si','정읍시'),(45190,'Namwon-si','남원시'),(45210,'Gimje-si','김제시'),(45710,'Wanju-gun','완주군'),(45720,'Jinan-gun','진안군'),(45730,'Muju-gun','무주군'),(45740,'Jangsu-gun','장수군'),(45750,'Imsil-gun','임실군'),(45770,'Sunchang-gun','순창군'),(45790,'Gochang-gun','고창군'),(45800,'Buan-gun','부안군'),(46110,'Mokpo-si','목포시'),(46130,'Yeosu-si','여수시'),(46150,'Suncheon-si','순천시'),(46170,'Naju-si','나주시'),(46230,'Gwangyang-si','광양시'),(46710,'Damyang-gun','담양군'),(46720,'Gokseong-gun','곡성군'),(46730,'Gurye-gun','구례군'),(46770,'Goheung-gun','고흥군'),(46780,'Boseong-gun','보성군'),(46790,'Hwasun-gun','화순군'),(46800,'Jangheung-gun','장흥군'),(46810,'Gangjin-gun','강진군'),(46820,'Haenam-gun','해남군'),(46830,'Yeongam-gun','영암군'),(46840,'Muan-gun','무안군'),(46860,'Hampyeong-gun','함평군'),(46870,'Yeonggwang-gun','영광군'),(46880,'Jangseong-gun','장성군'),(46890,'Wando-gun','완도군'),(46900,'Jindo-gun','진도군'),(46910,'Sinan-gun','신안군'),(47111,'Nam-gu, Pohang-si','포항시 남구'),(47113,'Buk-gu, Pohang-si','포항시 북구'),(47130,'Gyeongju-si','경주시'),(47150,'Gimcheon-si','김천시'),(47170,'Andong-si','안동시'),(47190,'Gumi-si','구미시'),(47210,'Yeongju-si','영주시'),(47230,'Yeongcheon-si','영천시'),(47250,'Sangju-si','상주시'),(47280,'Mungyeong-si','문경시'),(47290,'Gyeongsan-si','경산시'),(47730,'Uiseong-gun','의성군'),(47750,'Cheongsong-gun','청송군'),(47760,'Yeongyang-gun','영양군'),(47770,'Yeongdeok-gun','영덕군'),(47820,'Cheongdo-gun','청도군'),(47830,'Goryeong-gun','고령군'),(47840,'Seongju-gun','성주군'),(47850,'Chilgok-gun','칠곡군'),(47900,'Yecheon-gun','예천군'),(47920,'Bonghwa-gun','봉화군'),(47930,'Uljin-gun','울진군'),(47940,'Ulleung-gun','울릉군'),(48121,'Uichang-gu, Changwon-si','창원시 의창구'),(48123,'Seongsan-gu, Changwon-si','창원시 성산구'),(48125,'Masanhappo-gu, Changwon-si','창원시 마산합포구'),(48127,'Masanhoewon-gu, Changwon-si','창원시 마산회원구'),(48129,'Jinhae-gu, Changwon-si','창원시 진해구'),(48170,'Jinju-si','진주시'),(48220,'Tongyeong-si','통영시'),(48240,'Sacheon-si','사천시'),(48250,'Gimhae-si','김해시'),(48270,'Miryang-si','밀양시'),(48310,'Geoje-si','거제시'),(48330,'Yangsan-si','양산시'),(48720,'Uiryeong-gun','의령군'),(48730,'Haman-gun','함안군'),(48740,'Changnyeong-gun','창녕군'),(48820,'Goseong-gun','고성군'),(48840,'Namhae-gun','남해군'),(48850,'Hadong-gun','하동군'),(48860,'Sancheong-gun','산청군'),(48870,'Hamyang-gun','함양군'),(48880,'Geochang-gun','거창군'),(48890,'Hapcheon-gun','합천군'),(50110,'Jeju-si','제주시'),(50130,'Seogwipo-si','서귀포시'),(51110,'Chuncheon-si','춘천시'),(51130,'Wonju-si','원주시'),(51150,'Gangneung-si','강릉시'),(51170,'Donghae-si','동해시'),(51190,'Taebaek-si','태백시'),(51210,'Sokcho-si','속초시'),(51230,'Samcheok-si','삼척시'),(51720,'Hongcheon-gun','홍천군'),(51730,'Hoengseong-gun','횡성군'),(51750,'Yeongwol-gun','영월군'),(51760,'Pyeongchang-gun','평창군'),(51770,'Jeongseon-gun','정선군'),(51780,'Cheorwon-gun','철원군'),(51790,'Hwacheon-gun','화천군'),(51800,'Yanggu-gun','양구군'),(51810,'Inje-gun','인제군'),(51820,'Goseong-gun','고성군'),(51830,'Yangyang-gun','양양군');
/*!40000 ALTER TABLE `sigungu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-06  8:50:13
