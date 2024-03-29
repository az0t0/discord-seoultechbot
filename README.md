# TechBot Project - Discord Bot for SEOULTECH
## Introduction
discord.py를 이용하여 서울과학기술대학교의 식당의 메뉴와 공지사항을 자동으로 알려주고, 편의기능을 제공하는 Discord 봇 프로젝트 입니다.

학교 공지사항의 접근성을 높히고 빈번히 오작동하는 에브리타임 기능인 오늘의 학식을 대체하기 위해, 서울과기대 학우 분들이 많이 사용하는 메신저 'Discord'의 API를 이용하는 자동화 채팅 봇을 개발하기로 했습니다.

서울과학기술대학교 컴퓨터공학과의 2022학년도 2학기 전공선택 과목 '오픈소스소프트웨어', '데이터베이스'의 개인 프로젝트로 시작하여, 해당 코드를 사용한 봇을 배포했습니다.
스스로 사용할 목적으로 만든 프로젝트라서 꾸준히 유지보수, 기능 추가와 최적화를 거칠 계획입니다.


## Release
우측의 Releases를 클릭하여 이 프로젝트의 안정적인 버전을 사용한 '테크봇'을 초대할 수 있습니다.
봇/코드 업데이트 시 변경사항은 Releases와 [테크봇 공식 서버](https://discord.gg/wRXRHB7mr6)의 `#봇-공지`채널을 통해 안내할 예정입니다.


### Features and Commands
* 공지사항과 학식 자동 알림
  * 매일 자정 `/알림설정` 명령어를 사용한 채널에 오늘의 학사일정을 보냅니다.
  * 1시간 간격으로 학교 홈페이지의 학교공지사항, 학사공지, 장학공지, *생활관공지(선택)* 를 체크하여, 새 공지사항이 올라왔다면 `/알림설정` 명령어를 사용한 채널에 알림을 보냅니다.
  * 디스코드 서버의 관리자(혹은 메세지 관리 권한 소유자)가 지정한 시간에 제2학생회관과 테크노파크의 식단을 출력합니다.


* 봇 조작 명령어
  * `/도움`: 테크봇의 명령어 목록과 설명을 볼 수 있습니다.
  * `/알림설정 [학식알림] [생활관공지알림]`: 알림을 설정하는 명령어입니다. 해당 명령어를 입력한 채널이 각종 알림을 받을 채널이 됩니다.
    아래의 옵션에 따라 선택적으로 학식 메뉴 알림과 생활관 공지 알림을 받을 수 있습니다.
    * `[학식알림]`의 선택지: 받지 않음, 9시, 10시, 11시, 12시
    * `[생활관공지알림]`의 선택지: 받지 않음, 받음
    * **해당 명령어의 사용자는 관리자 권한이 있어야 합니다.**
    * 봇 초대 후 이 명령어를 입력하지 않으면 공지사항 알림, 학식 자동 알림, 학사일정 알림을 받을 수 없습니다. 아래의 명령어는 정상작동 합니다.
  * `/핑`: 명령어 입력 시점부터 메세지 전송까지 총 지연시간을 보여줍니다.


* 학교 생활 명령어
  * `/2학 [날짜]`: 제2학생회관의 오늘 식단(점심, 저녁)을 보여줍니다. 2023년 1월 28일 기준으로 점심의 간단 snack 메뉴는 항상 같으므로 생략합니다.
    * `[날짜]` 옵션으로 내일의 제2학생회관 식단을 확인 가능합니다.
  * `/테파`: 테크노파크의 이번 주 식단표를 이미지로 보여줍니다.
  * `/날씨`: 캠퍼스가 있는 공릉동의 날씨와 1 ~ 6시간 뒤 날씨 예보를 보여줍니다.


### Working Screenshots
#### 식단과 공지사항 푸시 알림
![/알림설정 명령어 사용](https://user-images.githubusercontent.com/113516890/210235310-7ca6037d-9979-40d5-828e-a04b8b5c59dd.png)

![공지사항 자동알림](https://user-images.githubusercontent.com/113516890/210235400-d9f9caa9-1e2e-4f36-a309-ae18b73eb85c.png)

#### 일정 알림
![오늘의 일정 자동 알림](https://user-images.githubusercontent.com/113516890/217039793-aaa4d150-f5fc-4881-af2c-e1735adcc5a0.png)

#### `/2학`, `/테파` 명령어 사용
![/테파 명령어 사용](https://user-images.githubusercontent.com/113516890/210235490-47ab2ff2-5b1c-437c-9df0-8c69d29d4b4c.png)

#### `/날씨` 명령어 사용
![/날씨 명령어 사용](https://user-images.githubusercontent.com/113516890/210235614-51a4259c-2635-4dae-b11b-030b99352573.png)

### Bug Report
문제 발생 시 반드시 **해당 서버, 채널의 ID와 함께** issue를 작성하거나, [테크봇 공식 서버](https://discord.gg/wRXRHB7mr6)의 피드백 채널에서 문제를 알려주시기 바랍니다.

---
## Getting Started with My Bot
명령어는 git과 python3이 설치된 Linux 환경을 기준으로 설명했으며, 명령어를 제외한 나머지 설명은 Windows 환경에서도 동일합니다.
### Get Code
```shell
$ git clone https://github.com/az0t0/discord-seoultechbot.git
```
git을 사용해 위의 명령어로 이 Repository를 clone하여 최신 버전의 코드를 받거나, Releases에서 안정적인 버전의 코드를 내려받을 수 있습니다.
### Require Packages
1. discord.py
2. requests
3. beautifulsoup4

해당 모듈은 `$ pip install -r discord-seoultechbot/techbot-packages.txt` 명령어로 한 번에 설치 가능합니다.


### Token
Discord 봇을 만들기 위해 Discord 계정, [Discord Developers Portal](https://discord.com/developers/)의 Applications > 내 앱 > Bot에서 모든 Intents 옵션과 토큰이 필요합니다.
또한 `/날씨` 명령어를 사용하려면 [오픈 API의 기상청 단기예보 조회서비스](https://www.data.go.kr/data/15084084/openapi.do)에서 인증키를 발급 받아야 합니다.

토큰을 요구하는 부분은 아래와 같습니다.

```python
...
import os
...
token_path = os.path.dirname(os.path.abspath(__file__)) + "/token"
token_file = open(token_path, "r", encoding="utf-8").read().split()
discord_bot_token = token_file[0]
weather_api_token = token_file[1]
...

...
@tree.command(description='...')
async def 날씨(interaction):
    try:
        await interaction.response.defer()
        date = weather.get_weather(weather_api_token)[0]
        data = weather.get_weather(weather_api_token)[1]
        ...
...
bot.run(discord_bot_token)
```
`discordbot.py`와 같은 경로에 `token` 파일(확장자 없음)을 만들어 첫번째 줄에는 **Discord 봇의 토큰**, 두번째 줄에는 오픈 API에서 발급받은 **일반 인증키**를 입력하면 됩니다.
**토큰 노출 예방을 위해 `token` 파일이 `.gitignore`에 추가 되어있는지 반드시 확인하세요.**

### Run
```shell
$ cd discord-seoultechbot/src
$ nohup python3 -u discordbot.py > discordbot.log 2>&1 &
```
백그라운드에서 봇이 실행되며, `discordbot.log` 파일에서 로그를 확인해볼 수 있습니다.
[Discord Developers Portal](https://discord.com/developers/)의 Applications > 내 앱 > OAuth2에서 bot 체크 후 생성되는 링크를 통해 봇을 초대할 수 있습니다.


---
## About Files
### Repository 내
* `discordbot.py`: Discord 봇의 동작에 필요한 핵심적인 코드입니다.
* `server_settings.py`: SQLite3을 이용하여 각 서버에서 설정한 알림 시간을 저장 및 수정하는 코드입니다.
* `menucrawler.py`: SQLite3과 requests, BeautifulSoup을 이용하여 학교/서울테크노파크 홈페이지에서 식단을 크롤링하고 데이터베이스에 저장, 불러오는 코드입니다.
* `noticecrawler.py`: SQLite3과 requests, BeautifulSoup을 이용하여 학교 공지사항과 일정을 크롤링하고 데이터베이스에 저장, 불러오는 코드입니다.
* `weather.py`: 정부의 오픈 API와 requests를 이용하여 캠퍼스의 날씨 예보를 불러오는 코드입니다.

### Runtime
* `food.db`: 학교 홈페이지에서 크롤링 한 식단을 저장하는 데이터베이스 파일입니다.
* `notice.db`: 학교 공지사항의 게시글 번호를 저장하는 데이터베이스 파일입니다.
* `server_settings.db`: 각 서버에서 설정한 알림 받을 채널의 ID를 저장하는 데이터베이스 파일입니다.

## License
* 이 프로젝트의 라이센스는 GNU GPL 3.0이며, 자세한 내용은 `LICENSE`를 참고하시기 바랍니다.