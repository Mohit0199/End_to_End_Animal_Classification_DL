function predictImage() {
  const fileInput = document.getElementById("imageUpload");
  const resultBox = document.getElementById("resultBox");

  if (!fileInput.files || fileInput.files.length === 0) {
    alert("Please upload an image first.");
    return;
  }

  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = function () {
    const base64Image = reader.result.split(",")[1];

    fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image: base64Image }),
    })
      .then((response) => response.json())
      .then((data) => {
        resultBox.innerText = "Prediction: " + data[0]["image"];
      })
      .catch((error) => {
        console.error("Error:", error);
        resultBox.innerText = "Error in prediction.";
      });
  };

  reader.readAsDataURL(file);
}

document.getElementById("imageUpload").addEventListener("change", function (event) {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = function () {
    const imgElement = document.getElementById("imagePreview");
    imgElement.src = reader.result;
  };

  if (file) {
    reader.readAsDataURL(file);
  }
});
