# 환경 변수 사용을 위해 필요
import os

# DB Connectors
import sqlite3
import mysql.connector

# 로거 가져오기
import seoultechbot
logger = seoultechbot.logger.setup('db-connector')


class DBConnector:
    config = 'seoultechbot_discord.db'
    conn = None

    def open_connection(self):
        """SQLite 데이터베이스 연결"""
        try:
            self.conn = sqlite3.connect(self.config)
            if self.conn.cursor():
                logger.info("로컬 SQLite DB(" + self.config + ")에 연결 완료")
        except sqlite3.Error as e:
            logger.error("로컬 SQLite DB(" + self.config + ")에 연결 실패: " + str(e))
            logger.error("DB에 연결할 수 없으므로 봇을 종료합니다.")
            exit(-1)

    def close_connection(self):
        """SQLite 데이터베이스 연결 끊기"""
        if self.conn is not None:
            self.conn.close()
            logger.info("로컬 SQLite DB(" + self.config + ")와 연결 종료")

    def execute_query(self, query):
        """SQL 쿼리 실행 및 결과 반환"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print("로컬 SQLite DB(" + self.config + ")에 쿼리 요청 오류: " + str(e))
        finally:
            cursor.close()


class MYSQLConnector(DBConnector):
    MYSQL_HOST = os.getenv("STBOT_MYSQL_HOST")
    MYSQL_PORT = os.getenv("STBOT_MYSQL_PORT", 3306)
    MYSQL_DB = os.getenv("STBOT_MYSQL_DB")
    MYSQL_USER = os.getenv("STBOT_MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("STBOT_MYSQL_PASSWORD")

    super.config = {
        'host': MYSQL_HOST,
        'port': MYSQL_PORT,
        'user': MYSQL_USER,
        'password': MYSQL_PASSWORD,
        'database': MYSQL_DB
    }

    def open_connection(self):
        """MySQL 데이터베이스 연결"""
        try:
            self.conn = mysql.connector.connect(**super.config)
            if self.conn.is_connected():
                logger.info("MySQL DB(HOST: " + self.MYSQL_HOST + ":" + self.MYSQL_PORT +
                            ", NAME: " + self.MYSQL_DB + ")에 연결 완료")
        except mysql.connector.Error as e:
            logger.error("MySQL DB(" + self.MYSQL_HOST + ")에 연결 실패: " + str(e))
            logger.error("DB에 연결할 수 없으므로 봇을 종료합니다.")
            exit(-1)

    def close_connection(self):
        """MySQL 데이터베이스 연결 끊기"""
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()
            logger.info("MySQL DB(HOST: " + self.MYSQL_HOST + ":" + self.MYSQL_PORT +
                        ", NAME: " + self.MYSQL_DB + ")와 연결 종료")

    def execute_query(self, query):
        """SQL 쿼리 실행 및 결과 반환"""
        if self.conn is not None and self.conn.is_connected():
            cursor = self.conn.cursor()
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except mysql.connector.Error as e:
                logger.error("MySQL DB(" + self.MYSQL_HOST + ")에 쿼리 요청 오류: " + str(e))
            finally:
                cursor.close()
        else:
            logger.warn("DB와 연결이 열리지 않았습니다. 쿼리 요청 전 연결을 먼저 해주세요.")

