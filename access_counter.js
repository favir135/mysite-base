// 非同期でサーバーからアクセスカウントを取得する
// 取得したカウントをページのカウンター要素に表示する
// エラー発生時はエラーメッセージを表示する
async function counter() {
    try {
        let response = await fetch("/count",
        );
        let data = await response.json();

        document.getElementById("counter").innerText = data.count;
    } catch (e) {
        document.getElementById("counter").innerText = "エラー";
        console.log(e);
    }
}

counter();