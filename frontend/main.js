document.addEventListener("DOMContentLoaded", () => {
    const tweetForm = document.getElementById('tweet-form');
    const tweetContent = document.getElementById('tweet-content');
    const tweetsContainer = document.getElementById('tweets');

    tweetForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const content = tweetContent.value;
        await fetch('http://localhost:8000/tweets/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content }),
        });
        tweetContent.value = '';
        loadTweets();
    });

    async function loadTweets() {
        const response = await fetch('http://localhost:8000/tweets/');
        const tweets = await response.json();
        tweetsContainer.innerHTML = '';
        tweets.forEach(tweet => {
            const tweetElement = document.createElement('div');
            tweetElement.textContent = `${tweet.content} - ${new Date(tweet.timestamp).toLocaleString()}`;
            tweetsContainer.appendChild(tweetElement);
        });
    }

    loadTweets();
});
