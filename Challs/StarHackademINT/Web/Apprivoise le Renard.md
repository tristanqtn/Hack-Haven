## La machine à cookies

![[Pasted image 20240906162729.png]]

The background color and this div prevent us from accessing the cookie machine :

```html
<div class="sign" id="forbidden-sign">
    <h3>Interdit aux renards</h3>
  </div>
```

So we delete them and enable the form to enable the cookie machine : 

![[Pasted image 20240906163049.png]]

Then we simply have to find the correct amount of cookies to bake : 

![[Pasted image 20240906163133.png]]

## Le Débugger et la Console

In the source code of the page we can see this list of ingredients : 

```js
  // Aucun renard ne trouvera jamais cette liste !
  var liste_des_ingredients = [
    "3reP4ehY89",
    "5gFdes3_i$Ll+",
    "56B4rstt5wx",
    "yzABeçàQG?",
    "I_QLM",
    "Sucres!",
    "OuiXpu@#?!",
    "àéösale",
  ];
```

This list is accessible from the console : 

![[Pasted image 20240906163352.png]]In the source files there's a JS file containing multiple functions that we can call from the console. We are interested in those functions : 

```js
const bakeCookies = (ingredients) => {
  let cookie;
  cookie = mix(ingredients);
  cookie = shake(cookie);
  cookie = addSugar(cookie);
  cookie = heat(cookie);
  cookie = present(cookie);
  return cookie;
};

const heat = (prep) => {
  let isRenard = true;
  let heated = "";
  for (let index = 0; index < prep.length; index = index + 3) {
    heated += prep[index];
  }

  heated = heated.slice(0, 12);

  if (isRenard) {
    heated = "Ha ha, tout a brûlé au four. Tu n'auras rien méchant Renard !";
  }
```

![[Pasted image 20240906163546.png]]

The problem is that the boolean `isRenard` is always true so we had a breakpoint just before the `  if (isRenard) {`. To place a breakpoint, go to the file and right click on the line number and click the `add breakpoint` button. 

The we rerun the command : `bakeCookies(liste_des_ingredients)` avec le bon breakpoint.

![[Pasted image 20240906163817.png]]

## Le Maître des Cookies 

![[Pasted image 20240906164112.png]]

After decrypting the base64 encoding of this cookie we obtain : `VHJ1ZQ==` = `True`
So now we encode : `False` = `RmFsc2U=`

Then we simply have to update the cookie and then refresh the page : 

![[Pasted image 20240906164300.png]]

## Livraison de Cookies 

![[Pasted image 20240906164404.png]]