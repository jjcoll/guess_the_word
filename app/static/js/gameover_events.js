document.querySelector('.play-again').addEventListener('click', (e) => {
    window.location.href = '/'
})


document.querySelectorAll('.about').forEach((element) => {
    element.addEventListener('click', (e) => {
        window.location.href = '/about'
    })
})
