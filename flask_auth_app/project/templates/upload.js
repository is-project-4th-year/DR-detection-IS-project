document.addEventListener('DOMContentLoaded', function() {
    const dropzone = document.getElementById('dropzone');
    const fileInput = dropzone.querySelector('input[type="file"]');
    const submitBtn = document.getElementById('submitBtn');

    // Enable submit button when a file is selected
    fileInput.addEventListener('change', function () {
        submitBtn.disabled = !fileInput.files.length;
    });

    // Drag over
    dropzone.addEventListener('dragover', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.add('dragover');
    });

    // Drag leave
    dropzone.addEventListener('dragleave', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove('dragover');
    });

    // Drop
    dropzone.addEventListener('drop', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove('dragover');
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
            submitBtn.disabled = false;
        }
    });

    // Clicking the dropzone triggers file input
    dropzone.addEventListener('click', function () {
        fileInput.click();
    });
});