const savedFilters = localStorage.getItem('savedFilters') || '[]';
const savedLocation = localStorage.getItem('savedLocation') || '';

document.querySelectorAll('input[name="interest"]').forEach(checkbox => {
  checkbox.checked = JSON.parse(savedFilters).includes(checkbox.value);
});

document.getElementById('loc').value = savedLocation;

function handleSubmit() {

  const selectedFilters = Array.from(document.querySelectorAll('input[name="interest"]:checked')).map(checkbox => checkbox.value);


  const location = document.getElementById('loc').value;

  localStorage.setItem('savedFilters', JSON.stringify(selectedFilters));
  localStorage.setItem('savedLocation', location);

  window.location.href = 'home.html';
}

document.getElementById('submitBtn').addEventListener('click', handleSubmit);
