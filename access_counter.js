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