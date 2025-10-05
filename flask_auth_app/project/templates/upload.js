document.addEventListener('DOMContentLoaded', function() {
    const dropzone = document.getElementById('dropzone');
    const fileInput = dropzone.querySelector('input[type="file"]');
    const submitBtn = document.getElementById('submitBtn');
    let fileSelected = false;

    dropzone.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', () => {
        fileSelected = fileInput.files.length > 0;
        submitBtn.disabled = !fileSelected;
    });

    dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.classList.add('dragover');
    });
    dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('dragover');
    });
    dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.classList.remove('dragover');
        fileInput.files = e.dataTransfer.files;
        fileSelected = fileInput.files.length > 0;
        submitBtn.disabled = !fileSelected;
    });
});