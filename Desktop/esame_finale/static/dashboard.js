document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".tab-button");
  const contents = document.querySelectorAll(".tab-content");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const tab = button.dataset.tab;

      buttons.forEach(btn => {
        btn.classList.remove("active", "bg-blue-500", "text-white");
        btn.classList.add("bg-gray-300");
      });

      button.classList.add("active", "bg-blue-500", "text-white");
      button.classList.remove("bg-gray-300");

      contents.forEach(content => {
        content.classList.add("hidden");
      });

      document.getElementById(tab).classList.remove("hidden");
    });
  });
});
