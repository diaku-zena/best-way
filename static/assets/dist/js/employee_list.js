// JavaScript code to handle dynamic searching and pagination using Fetch API
let totalPages = 0;
const employeeTableBody = document.getElementById('employeeTableBody');
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

async function fetchEmployees() {
    const response = await fetch(`employee-list-ajax/${currentPage}`);
    const data = await response.json();
    displayEmployees(data.results);
    displayPagination(data.count);
}

function displayEmployees(employees) {  
    employeeTableBody.innerHTML = '';
    employees.forEach(employee => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${employee.numero_mecanografico || ''}</td>
            <td>${employee.firstname} ${employee.surname}</td>
            <td>${employee.date_of_birth}</td>
            <td>${employee.personnel_number}</td>
            <td>${employee.estado_civil}</td> 
            <td>${employee.morada || ''}</td>
            <td>
                <span class="text-center"><a href="employee-edit/${employee.id}" type="button" class="btn iq-bg-warning btn-rounded btn-sm my-0"><i class="fa fa-pencil" aria-hidden="false"></i></a></span>
                <span class=""><a href="employee-detail/${employee.id}" type="button" class="btn iq-bg-primary btn-rounded btn-sm my-0"><i class="fa fa-eye" aria-hidden="true"></i></a></span>
                <span class=""><a href="employee-delete/${employee.id}" type="submit"  data-toggle="modal" data-target="#exampleModal3" type="button" class="btn iq-bg-danger btn-rounded btn-sm my-0" ><i class="fa fa-trash" aria-hidden="true"></i></a></span>
            </td>`;
        employeeTableBody.appendChild(tr); 
    });
}





function displayPagination(totalCount) {
    totalPages = Math.ceil(totalCount / 100); // Assuming 10 employees per page
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
        await fetchEmployees();
        hideProgressBar(); // Hide progress bar after fetching data
    }
}

fetchEmployees();