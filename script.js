document.addEventListener("DOMContentLoaded", function () {
    const uploadArea = document.getElementById("upload-area");
    const fileInput = document.getElementById("resume");
  
    if (uploadArea && fileInput) {
      // Click to open file dialog
      uploadArea.addEventListener("click", function () {
        fileInput.click();
      });
  
      // Drag over effect
      uploadArea.addEventListener("dragover", function (e) {
        e.preventDefault();
        uploadArea.classList.add("dragover");
      });
  
      // Drag leave effect
      uploadArea.addEventListener("dragleave", function () {
        uploadArea.classList.remove("dragover");
      });
  
      // Handle file drop
      uploadArea.addEventListener("drop", function (e) {
        e.preventDefault();
        fileInput.files = e.dataTransfer.files;
        uploadArea.classList.remove("dragover");
  
        if (e.dataTransfer.files.length > 0) {
          uploadArea.querySelector(".upload-text").textContent =
            "File selected: " + e.dataTransfer.files[0].name;
        }
      });
    }
  });