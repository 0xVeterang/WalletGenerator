import os
from eth_account import Account

def generate_keypair():
    # 키 쌍 생성
    account = Account.create()
    return account.address, account._private_key.hex()  # _private_key 사용

def save_keys(address, private_key):
    # 파일에 주소와 개인 키 저장 (파일 이름 변경)
    with open(f'{address}.txt', 'a') as file:
        file.write(f'Address: {address}, Private Key: {private_key}\n')

def main():
    while True:
        address, private_key = generate_keypair()
        # 공개 키의 끝 6자리를 확인
        if address[-6:] == address[-1] * 6:  # 마지막 6자리가 동일한지 확인
            print(f'Found: {address} with Private Key: {private_key}')
            save_keys(address, private_key)
            break  # 종료

if __name__ == "__main__":
    main()
