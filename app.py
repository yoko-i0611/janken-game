from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__, static_url_path='', static_folder='static')

# じゃんけんの選択肢と対応する画像ファイル名
CHOICES = {
    'グー': 'rock.png',
    'チョキ': 'scissors.png',
    'パー': 'paper.png'
}

def test_all_combinations():
    """全ての組み合わせをテストする関数"""
    choices = ['グー', 'チョキ', 'パー']
    print("\n=== じゃんけん判定テスト ===")
    for p in choices:
        for c in choices:
            result = determine_winner(p, c)
            print(f"プレイヤー: {p} vs コンピュータ: {c} => {result}")
    print("========================\n")

def determine_winner(player, computer):
    # デバッグ用ログ出力
    print(f"プレイヤーの選択: {player}")
    print(f"コンピュータの選択: {computer}")
    
    # あいこの場合
    if player == computer:
        print("結果: あいこ")
        return 'あいこです！'
    
    # プレイヤーが勝つ場合の条件
    player_wins = (
        (player == 'グー' and computer == 'チョキ') or
        (player == 'チョキ' and computer == 'パー') or
        (player == 'パー' and computer == 'グー')
    )
    
    result = 'あなたの勝ちです！' if player_wins else 'コンピュータの勝ちです！'
    
    # デバッグ出力
    print(f"判定結果: プレイヤーの勝利? {player_wins}")
    print(f"最終結果: {result}")
    
    return result

@app.route('/')
def index():
    # 起動時に全ての組み合わせをテスト
    test_all_combinations()
    return render_template('index.html')

@app.route('/play/<choice>')
def play(choice):
    # コンピュータの選択
    computer_choice = random.choice(list(CHOICES.keys()))
    
    # 勝敗判定
    result = determine_winner(choice, computer_choice)
    
    # レスポンスデータを作成
    response_data = {
        'result': result,
        'player_choice': choice,
        'computer_choice': computer_choice,
        'player_choice_img': CHOICES[choice],
        'computer_choice_img': CHOICES[computer_choice]
    }
    
    # デバッグ用ログ出力
    print("レスポンスデータ:", response_data)
    
    # JSONレスポンスを返す
    return jsonify(response_data)

if __name__ == '__main__':
    # 環境変数からポート番号を取得（Herokuで必要）
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 