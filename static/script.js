document.getElementById('fetch-data').addEventListener('click', () => {
    fetch('/get-data')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('#dataset-table tbody');
            tbody.textContent = ''; // Clear previous rows

            data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${row.Age_Range}</td>
                    <td>${row.Gender_of_the_patient_Male === 1 ? 'Male' : 'Female'}</td>
                    <td>${row.Protected_Result.toFixed(2)}</td>
                `;
                tbody.appendChild(tr);
            });
        });
});
