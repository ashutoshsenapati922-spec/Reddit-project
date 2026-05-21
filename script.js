const API = "http://127.0.0.1:8000"

async function createPost(){

    let title =
    document.getElementById("title").value

    let content =
    document.getElementById("content").value

    await fetch(`${API}/post?title=${title}&content=${content}`,{
        method:"POST"
    })

    loadPosts()
}

async function loadPosts(){

    let res = await fetch(`${API}/posts`)

    let posts = await res.json()

    let output = ""

    posts.forEach(post => {

        output += `
        <div class="post">
            <h2>${post.title}</h2>

            <p>${post.content}</p>

            <h3>Votes: ${post.votes}</h3>

            <button onclick="vote(${post.id},1)">
                ⬆ Upvote
            </button>

            <button onclick="vote(${post.id},-1)">
                ⬇ Downvote
            </button>
        </div>
        `
    })

    document.getElementById("posts").innerHTML = output
}

async function vote(id,type){

    await fetch(
    `${API}/vote/${id}?vote_type=${type}`,
    {
        method:"POST"
    })

    loadPosts()
}

loadPosts()