import os
from eth_account import Account
from concurrent.futures import ThreadPoolExecutor

def generate_keypair():
    # 키 쌍 생성
    account = Account.create()
    return account.address, account._private_key.hex()  # _private_key 사용

def has_matching_pattern(address):
    # 공개 키의 3번째 자리부터 4개와 끝 4자리가 동일한지 확인
    middle_chars = address[2:6].lower()  # 3번째 자리부터 4개
    last_chars = address[-4:].lower()  # 끝 4자리
    print(f'middle = {middle_chars},  last = {last_chars}')
    return middle_chars == last_chars and len(set(middle_chars)) == 1

def process_keypair():
    address, private_key = generate_keypair()
    if has_matching_pattern(address):
        return address, private_key
    return None

def main():
    count = 0  # 생성된 키 쌍 수를 기록합니다.
    found_keypair = None

    # ThreadPoolExecutor를 사용하여 병렬 처리
    with ThreadPoolExecutor(max_workers=8) as executor:
        while found_keypair is None:
            # 100개의 키 쌍을 동시에 생성
            futures = [executor.submit(process_keypair) for _ in range(100)]
            for future in futures:
                result = future.result()
                if result:
                    found_keypair = result
                    break
            count += 100  # 생성된 키 쌍 수를 업데이트

    address, private_key = found_keypair
    print(f'Found: {address} with Private Key: {private_key} after generating {count} keys')

    # 파일에 주소와 개인 키 저장
    with open(f'{address}.txt', 'a') as file:
        file.write(f'Address: {address}, Private Key: {private_key}\n')

if __name__ == "__main__":
    main()
