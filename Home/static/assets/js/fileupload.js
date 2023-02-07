window.addEventListener('load', () => {
    const preview = document.querySelector('#previewimg')
    const profile = document.querySelector('#profileimg')
    profile.addEventListener('change', (event) => {
        const [file] = event.target.files
        if(file){
            preview.src=URL.createObjectURL(file)
        }
    })
})