fetch('include/header.html')
  .then((response) => {
    return response.text();
  })
  .then((data) => {
    document.querySelector('header').innerHTML = data;
  });
