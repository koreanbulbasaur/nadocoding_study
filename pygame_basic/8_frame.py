import pygame
##########################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()
##########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 이미지 불러오기

# 캐릭터(스프라이트) 불러오기

# 이동할 좌표

# 이동 속도

# 적 enemy 캐릭터

# 폰트 정의

# 총 시간

# 시간 시간
start_ticks = pygame.time.get_ticks()  # 현재 tick을 받아옴

# 이벤트 루프
running = True
while running:
    dt = clock.tick(120)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()  # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()
