fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('data-container');
    data.forEach(item => {
      const element = document.createElement('div');
      element.textContent = item.name; 
      container.appendChild(element);
    });
  })
  .catch(error => console.error('Error:', error));
