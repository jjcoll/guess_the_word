
const lightSvg = '<svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" /></svg>'


const darkSvg = '<svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" /></svg>'




const switchThemeBtn = document.querySelector('.switch-theme-btn')
switchThemeBtn.addEventListener('click', (e) => {

    if (switchThemeBtn.id === 'light-icon') {
        switchThemeBtn.innerHTML = darkSvg
        switchThemeBtn.id = 'dark-icon'
        document.querySelector('html').setAttribute('data-bs-theme', 'dark')
    } else {
        switchThemeBtn.innerHTML = lightSvg
        switchThemeBtn.id = 'light-icon'
        document.querySelector('html').setAttribute('data-bs-theme', "")
    }

    // update the theme for the session
    fetch('/change-theme', {
        method: "POST",
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({ theme: switchThemeBtn.id })
    }).then(response => response.json()).then(data => {
        console.log(data)
    }).catch(error => console.log('Error: ', error))

    console.log(switchThemeBtn.id)
})



// set theme from on load
window.addEventListener('load', (e) => {
    // print active theme
    fetch('/theme').then(response => {
        if (!response.ok) {
            throw new Error('An error occured')
        }

        return response.json()
    }).then(data => {

        console.log(data.theme)

        if (data.theme) {

            if (data.theme === 'light-icon') {

                switchThemeBtn.innerHTML = lightSvg
                switchThemeBtn.id = 'light-icon'
                document.querySelector('html').setAttribute('data-bs-theme', "")
            } else {
                switchThemeBtn.innerHTML = darkSvg
                switchThemeBtn.id = 'dark-icon'
                document.querySelector('html').setAttribute('data-bs-theme', 'dark')
            }

        } else {
            console.log('No theme')
        }
    })
})