document.addEventListener('DOMContentLoaded', function() {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('imageInput');
    const submitBtn = document.getElementById('submitBtn');
    const dropzoneText = dropzone.querySelector('.dropzone-text');

    // Create preview image and remove button
    let previewImg = document.createElement('img');
    previewImg.className = 'preview-image';
    previewImg.style.display = 'none';

    let removeBtn = document.createElement('button');
    removeBtn.type = 'button';
    removeBtn.textContent = '✕';
    removeBtn.className = 'remove-preview-btn';
    removeBtn.style.display = 'none';

    // Remove image handler
    removeBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        previewImg.style.display = 'none';
        removeBtn.style.display = 'none';
        fileInput.value = '';
        submitBtn.disabled = true;
        if (dropzoneText) dropzoneText.style.display = '';
    });

    dropzone.appendChild(previewImg);
    dropzone.appendChild(removeBtn);

    function showPreview(file) {
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImg.src = e.target.result;
                previewImg.style.display = 'block';
                removeBtn.style.display = 'block';
                if (dropzoneText) dropzoneText.style.display = 'none';
            };
            reader.readAsDataURL(file);
        } else {
            previewImg.style.display = 'none';
            removeBtn.style.display = 'none';
            if (dropzoneText) dropzoneText.style.display = '';
        }
    }

    fileInput.addEventListener('change', function () {
        submitBtn.disabled = !fileInput.files.length;
        showPreview(fileInput.files[0]);
    });

    dropzone.addEventListener('dragover', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.add('dragover');
    });

    dropzone.addEventListener('dragleave', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove('dragover');
    });

    dropzone.addEventListener('drop', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove('dragover');
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
            submitBtn.disabled = false;
            showPreview(e.dataTransfer.files[0]);
        }
    });
});