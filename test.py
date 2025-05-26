import random

def janken():
    # じゃんけんの選択肢
    choices = ['グー', 'チョキ', 'パー']
    
    print("=== コンピュータとじゃんけんをしましょう！ ===")
    print("0: グー")
    print("1: チョキ")
    print("2: パー")
    
    while True:
        try:
            # プレイヤーの選択
            player_choice = int(input("\nあなたの選択を入力してください (0-2): "))
            if player_choice not in [0, 1, 2]:
                print("0, 1, 2 のいずれかを入力してください。")
                continue
                
            # コンピュータの選択（ランダム）
            computer_choice = random.randint(0, 2)
            
            # それぞれの選択を表示
            print(f"\nあなた: {choices[player_choice]}")
            print(f"コンピュータ: {choices[computer_choice]}")
            
            # 勝敗判定
            if player_choice == computer_choice:
                print("結果: あいこです！")
            elif (player_choice == 0 and computer_choice == 1) or \
                 (player_choice == 1 and computer_choice == 2) or \
                 (player_choice == 2 and computer_choice == 0):
                print("結果: あなたの勝ちです！おめでとう！")
            else:
                print("結果: コンピュータの勝ちです！")
            
            # もう一度プレイするか確認
            play_again = input("\nもう一度プレイしますか？ (y/n): ")
            if play_again.lower() != 'y':
                print("\nゲームを終了します。お疲れ様でした！")
                break
                
        except ValueError:
            print("無効な入力です。0, 1, 2 のいずれかを入力してください。")

if __name__ == "__main__":
    janken()
