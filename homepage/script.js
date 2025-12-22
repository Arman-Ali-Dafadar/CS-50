if (window.location.pathname.endsWith("quiz-q1.html"))
{
    localStorage.setItem("score", 0);
    console.log(localStorage.getItem("score"));
}

function q1(answer)
{
    if (answer==='c')
    {
        let result = parseInt(localStorage.getItem("score"));
        result++;
        localStorage.setItem("score", result);
        console.log(localStorage.getItem("score"));
    }
    window.location.href = "quiz-q2.html";
}

function q2(answer)
{
    if (answer==='b')
    {
        let result = parseInt(localStorage.getItem("score"));
        result++;
        localStorage.setItem("score", result);
        console.log(localStorage.getItem("score"));
    }
    window.location.href = "quiz-q3.html";
}

function q3(answer)
{
    if (answer==='a')
    {
        let result = parseInt(localStorage.getItem("score"));
        result++;
        localStorage.setItem("score", result);
        console.log(localStorage.getItem("score"));
    }
    window.location.href = "quiz-q4.html";
}

function q4(answer)
{
    if (answer==='d')
    {
        let result = parseInt(localStorage.getItem("score"));
        result++;
        localStorage.setItem("score", result);
        console.log(localStorage.getItem("score"));
    }
    window.location.href = "quiz-q5.html";
}

function q5(answer)
{
    if (answer==='c')
    {
        let result = parseInt(localStorage.getItem("score"));
        result++;
        localStorage.setItem("score", result);
        console.log(localStorage.getItem("score"));
    }
    window.location.href = "finalpage.html";
}

function Final()
{
    let result = parseInt(localStorage.getItem("score"));
    let user = ""

    if (result<=1)
    {
        user = ("You are new to the World of Anime.");
    }
    else if (result>=2 && result<5)
    {
        user = ("You are a Regular viewer.");
    }
    else if (result==5)
    {
        user = ("You are a otaku.");
    }

    document.getElementById("rank1").innerText=`You have answered ${result} questions correctly out of 5.`;
    document.getElementById("rank2").innerText=`${user}`;
    localStorage.clear();
}
