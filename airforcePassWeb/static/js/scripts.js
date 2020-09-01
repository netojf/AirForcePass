
//#region glitch1
    let bg = document.getElementById('glitch-container1');
    const container1count = 20;

    for (let i = 0; i < container1count; i++ ){
        let glitchBox = document.createElement('div');
        glitchBox.className = 'box';
        if(glitchBox && bg)
        {
            bg.appendChild(glitchBox);
        }
    }

    let glitch1 = document.getElementsByClassName('box');
    setInterval(function() {
        
        for(let i = 0; i < glitch1.length; i++){
            if(glitch1[i])
            {
                glitch1[i].style.left = Math.floor(Math.random()*20) + 'px';
                glitch1[i].style.top = Math.floor(Math.random()*20)+ 'px';
                glitch1[i].style.width = Math.floor(Math.random()*100)+ 'vw';
                glitch1[i].style.height = Math.floor(Math.random()*100)+ 'vh';
                glitch1[i].style.backgroundPosition = Math.floor(Math.random()*50)+ 'px';
            }
        }
    }, 200);
//#endregion

//#region glitch

window.onload = (event) => {

    let containers = document.getElementsByClassName('glitch-container');
    const count = 2;

    for (let index = 0; index < containers.length; index++) {
        container = containers[index]; 
        imgs = container.getElementsByClassName('glitch-img');
        
        for (let j = 0; j < imgs.length; j++) {
            img = imgs[j];
            style = getComputedStyle(img);
            container.height = style.height; 

            if (img && img.tagName==='IMG' && style) {
                for (let i = 0; i < count; i++ ){
                    let glitch = document.createElement('img');

                    glitch.src = img.src;
                    glitch.className = 'glitch';

                    glitch.style.position = 'absolute';

                    glitch.style.top = style.top;
                    glitch.style.height = style.height ;
                    glitch.style.width = style.width;
                    glitch.style.left = style.left ;
                    glitch.style.zIndex = 1000 + i;
                    
                    container.style.height +=  img.height + 'px';
                    container.appendChild(glitch);
                    
                }
            }
        }
    }

    let glitch = document.getElementsByClassName('glitch');
    setInterval(function() {
        for(let i = 0; i < glitch.length; i++){
            glitch[i].style.clipPath  = `inset(${Math.floor(Math.random()*100)}% ${Math.floor(Math.random()*80)}% ${Math.floor(Math.random()*100)}% ${Math.floor(Math.random()*80)}%)`;
            glitch[i].style.filter = `blur(${Math.floor(Math.random()*10)}px) invert(48%) sepia(13%) saturate(3207%) hue-rotate(130deg) brightness(95%) contrast(80%)`;
            glitch[i].style.opacity = `${Math.random()}`;
        }
    }, 75);
}
    
//#endregion


//#region TypeWriter

document.addEventListener('DOMContentLoaded', (event) => {
        
    let typedTextSpan = document.getElementsByClassName('typed-text')[0];

    const textArray = typedTextSpan.textContent.split('|');
    typedTextSpan.textContent = ''; 

    let cursorSpan = document.createElement("span");
    cursorSpan.className = 'cursor';
    cursorSpan.innerHTML = '&nbsp'; 
    const typingDelay = 75;
    const erasingDelay = 75;
    const newTextDelay = 500; // Delay between current and next text
    let textArrayIndex = 0;
    let charIndex = 0;

    typeWriterContainer = document.getElementsByClassName('typewriter-container');

    for (let index = 0; index < typeWriterContainer.length; index++) {

        staticTexts = typeWriterContainer[index].getElementsByClassName("static-typed-text");
        console.log(staticTexts);

        for (let i = 0; i < staticTexts.length; i++) {
            staticTexts[i].appendChild(cursorSpan); 
        }
    }



    function type() {
    if (charIndex < textArray[textArrayIndex].length) {
        if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
        typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, typingDelay);
    } 
    else {
        cursorSpan.classList.remove("typing");
        setTimeout(erase, newTextDelay);
    }
    }

    function erase() {
        if (charIndex > 0) {
        if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
        typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
        charIndex--;
        setTimeout(erase, erasingDelay);
    } 
    else {
        cursorSpan.classList.remove("typing");
        textArrayIndex++;
        if(textArrayIndex>=textArray.length) textArrayIndex=0;
        setTimeout(type, typingDelay + 1100);
    }
    }

    if(textArray.length) setTimeout(type, newTextDelay + 250);
});


//#endregion
