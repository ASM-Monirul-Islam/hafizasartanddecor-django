// Header Script

const bar = document.querySelector("#bar");
const navbar = document.querySelector("#navbar");
const close = document.querySelector("#close");

if (bar) {
  bar.addEventListener("click", () => {
    navbar.classList.add("active");
  });
}

if (close) {
  close.addEventListener("click", () => {
    navbar.classList.remove("active");
  });
}

document.addEventListener("click", (e) => {
  if (
    navbar.classList.contains("active") &&
    !bar.contains(e.target) &&
    !close.contains(e.target)
  ) {
    navbar.classList.remove("active");
  }
});

// Homepage Script

function filterProduct() {
  const product_category = document.querySelector("#category").value;
  const products = document.querySelectorAll(".product");

  products.forEach((product) => {
    if (product_category == "all") {
      product.style.display = "block";
    } else {
      if (product.dataset.category == product_category) {
        product.style.display = "block";
      } else {
        product.style.display = "none";
      }
    }
  });
}

// get_product.html

const quantity_container = document.querySelectorAll(
  ".quantity_container_child",
);

quantity_container.forEach((prod) => {
  const minus = prod.querySelector(".minus");
  const plus = prod.querySelector(".plus");
  const quantity = prod.querySelector(".quantity");

  quantity.value = "1";

  plus.addEventListener("click", () => {
    quantity.value = parseInt(quantity.value) + 1;
  });

  minus.addEventListener("click", () => {
    if (parseInt(quantity.value) > 1) {
      quantity.value = parseInt(quantity.value) - 1;
    }
  });
});

// Table Script

document.querySelectorAll("table tr").forEach((row) => {
  row.addEventListener("click", (e) => {
    if (e.target.closest("button, select, a, input")) return;
    row.classList.toggle("active");
  });
});

// confirm.html

const modal = document.getElementById("confirmModal");
const confirmBtn = document.getElementById("confirmBtn");
const cancelBtn = document.getElementById("cancelBtn");

let currentAction = {};

document.addEventListener("click", function (e) {
  const trigger = e.target.closest(".confirm-action");
  if (!trigger) return;

  e.preventDefault();

  currentAction = {
    url: trigger.dataset.url,
    method: trigger.dataset.method || "GET",
    title: trigger.dataset.title || "Are you sure?",
    message: trigger.dataset.message || "This action cannot be undone.",
  };

  document.getElementById("confirmTitle").innerText = currentAction.title;
  document.getElementById("confirmMessage").innerText = currentAction.message;

  modal.classList.remove("hidden");
});

cancelBtn.onclick = () => {
  modal.classList.add("hidden");
};

confirmBtn.onclick = () => {
  if (currentAction.method === "POST") {
    const form = document.getElementById("globalForm");
    form.action = currentAction.url;
    form.submit();
  } else {
    window.location.href = currentAction.url;
  }
};


// checkout.html

document.addEventListener("DOMContentLoaded", function () {
    const priceCells = document.querySelectorAll(".order_unit_price");
    const shippingRadios = document.querySelectorAll(".shipping_radio");

    const subtotalEl = document.querySelector(".unit_price");
    const deliveryEl = document.querySelector(".delivery_charge");
    const totalEl = document.querySelector(".total_price");

    let subtotal = 0;

    priceCells.forEach(cell => {
        let priceText = cell.textContent.trim();

        let price = parseFloat(priceText.replace(/[^0-9.]/g, ""));

        if (!isNaN(price)) {
            subtotal += price;
        }
    });

    subtotalEl.textContent = subtotal.toFixed(2);

    function updateTotal(deliveryCharge) {
        deliveryEl.textContent = deliveryCharge.toFixed(2);

        let total = subtotal + deliveryCharge;
        totalEl.textContent = total.toFixed(2);
    }

    shippingRadios.forEach(radio => {
        radio.addEventListener("change", function () {
            let deliveryCharge = 0;

            if (this.value === "Deliver Inside Dhaka") {
                deliveryCharge = 70;
            } else if (this.value === "Deliver Outside Dhaka") {
                deliveryCharge = 120;
            }

            updateTotal(deliveryCharge);
        });
    });

    if (shippingRadios.length > 0) {
        shippingRadios[0].checked = true;
        shippingRadios[0].dispatchEvent(new Event("change"));
    }
});