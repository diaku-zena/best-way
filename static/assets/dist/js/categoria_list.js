// JavaScript code to handle dynamic searching and pagination using Fetch API
let totalPages = 0;
const categoriaTableBody = document.getElementById('categoriaTableBody');
const paginationControls = document.getElementById('paginationControls');
let currentPage = 1;
const progressBar = document.getElementById('progressBar');

// Function to show progress bar
function showProgressBar() {
    progressBar.style.display = 'block';
}

// Function to hide progress bar
function hideProgressBar() {
    progressBar.style.display = 'none';
}

function displayCategorias(categorias) {  
    categoriaTableBody.innerHTML = '';
    categorias.forEach(categoria => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
           
            <td>${categoria.nome || ''}</td>
            
            <td>
                <span class="text-center"><a href="categoria-edit/${categoria.id}" type="button" class="btn iq-bg-warning btn-rounded btn-sm my-0"><i class="fa fa-pencil" aria-hidden="false"></i></a></span>
                <span class=""><a href="categoria-detail/${categoria.id}" type="button" class="btn iq-bg-primary btn-rounded btn-sm my-0"><i class="fa fa-eye" aria-hidden="true"></i></a></span>
                <span class=""><a href="categoria-delete/${categoria.id}" type="submit"  data-toggle="modal" data-target="#exampleModal3" type="button" class="btn iq-bg-danger btn-rounded btn-sm my-0" ><i class="fa fa-trash" aria-hidden="true"></i></a></span>
            </td>`;
        categoriaTableBody.appendChild(tr); 
    });
}
async function fetchCategorias() {
    const response = await fetch(`categoria-laboral-ajax/${currentPage}`);
    const data = await response.json();
    displayCategorias(data.results);
    displayPagination(data.count);
}







function displayPagination(totalCount) {
    totalPages = Math.ceil(totalCount / 10); // Assuming 10 employees per page
    paginationControls.innerHTML = '';

    // Previous button
    const previousButton = document.createElement('li');
    previousButton.classList.add('page-item');
    if (currentPage === 1) {
        previousButton.classList.add('disabled');
    }
    previousButton.innerHTML = `<a class="page-link" href="#" tabindex="-1" aria-disabled="true" onclick="navigatePage(${currentPage - 1})">Anterior</a>`;
    paginationControls.appendChild(previousButton);

    // Page numbers
    for (let i = 1; i <= totalPages; i++) {
        const button = document.createElement('li');
        button.classList.add('page-item');
        if (i === currentPage) {
            button.classList.add('active');
        }
        button.innerHTML = `<a class="page-link" href="#" onclick="navigatePage(${i})">${i}</a>`;
        paginationControls.appendChild(button);
    }

    // Next button
    const nextButton = document.createElement('li');
    nextButton.classList.add('page-item');
    if (currentPage === totalPages) {
        nextButton.classList.add('disabled');
    }
    nextButton.innerHTML = `<a class="page-link" href="#"  onclick="navigatePage(${currentPage + 1})">Próximo</a>`;
    paginationControls.appendChild(nextButton);
}

// Function to navigate to a specific page
// Function to navigate to a specific page and fetch data
async function navigatePage(page) {
    if (page >= 1 && page <= totalPages) {
        currentPage = page;
        showProgressBar(); // Show progress bar before fetching data
        await fetchCategorias();
        hideProgressBar(); // Hide progress bar after fetching data
    }
}

fetchCategorias();