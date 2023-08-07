let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        //{ className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        // { orderable: false, targets: [5, 6] },
        //{ searchable: false, targets: [0, 5, 6] }
    ],
    pageLength: 10,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listPropiedades();

    dataTable = $("#datatable-propiedades").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listPropiedades = async () => {
    try {
        const response = await fetch("http://localhost:8000/administracion/list_propiedades");
        const data = await response.json();
        console.log(data.propiedades)

        let content = ``;
        data.propiedades.forEach((propiedad, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${propiedad.id}</td>
                    <td>${propiedad.codigo_interno}</td>
                    <td>${propiedad.calle} ${propiedad.altura}</td>
                    <td>${propiedad.tipo_operacion}</td>
                    <td>${propiedad.tipo_propiedad}</td>
                    <td>${propiedad.tipo_provincia}</td>
                    <td>${propiedad.tipo_barrio}</td>
                    <td>${propiedad.tipo_ambiente}</td>
                    <td>${propiedad.moneda} ${propiedad.valor}</td>
                    <td>${propiedad.fecha_alta}</td>
                    
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button>
                        <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>`;
        });
        tableBody_propiedades.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});
