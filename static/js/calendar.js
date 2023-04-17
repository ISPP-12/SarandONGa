
// CALENDAR OPTIONS

let buttonText = {
    today: 'Hoy',
    year: 'Año',
    month: 'Mes',
    week: 'Semana',
    day: 'Día',
}

let customButtons = {
    calendarButton: {
        icon: 'bi bi-calendar',
        click: function () {
            alert('clicked the custom button!');
        },
        disabled: true,
    },
    listButton: {
        icon: 'bi bi-list-ul',
        click: function () {
            alert('clicked the custom button!');
        },
    },
}

let headerToolbar = {
    left: 'title',
    center: 'prev,next prevYear,nextYear today',
    right: 'calendarButton,dayGridMonth,dayGridYear listButton,listMonth,listYear'
}

let specificViewOptions = {
    dayGridYear: {
        titleFormat: { year: 'numeric' },
    },
    dayGridMonth: {
        titleFormat: { year: 'numeric', month: 'long' },
    },
    listMonth: {
        titleFormat: { year: 'numeric', month: 'long' },
    },
    listYear: {
        titleFormat: { year: 'numeric' },
    },
}

let onEventClick = (info) => {
    console.log('Event: ' + info.event.title);
    console.log('Event Start: ' + info.event.start);
    console.log('Event End (none): ' + info.event.end);
    console.log('Id: ' + info.event.extendedProps.id);

    // Properties from payment model
    console.log('PAGO');
    console.log('Cantidad: ' + info.event.extendedProps.amount);
    console.log('Observaciones: ' + info.event.extendedProps.observations);
    console.log('Pagado: ' + info.event.extendedProps.paid);

    // Properties from service model
    console.log('SERVICIO');
    console.log('Asistencia: ' + info.event.extendedProps.attendance);
    console.log('Tipo de servicio: ' + info.event.extendedProps.service_type);
    console.log('Usiario: ' + info.event.extendedProps.user);
    console.log('Pago: ' + info.event.extendedProps.payment);

    console.log('---------------------------------')
}

// FUNCTIONS

let setupCalendar = () => {
    let calendarEl = document.getElementById('calendar');

    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'es',
        themeSystem: 'bootstrap5',
        firstDay: 1,
        buttonText: buttonText,
        headerToolbar: headerToolbar,
        fixedWeekCount: false,
        events: events,
        views: specificViewOptions,
        customButtons: customButtons,
        eventClick: onEventClick,
    });
    calendar.render();
}

let disableToolbarButtons = () => {
    let calendarButton = document.querySelector('.fc-calendarButton-button');
    let listButton = document.querySelector('.fc-listButton-button');

    calendarButton.disabled = true;
    listButton.disabled = true;
}

let translateEmptyList = () => {
    let emptyList = document.querySelector('.fc-list-empty-cushion');

    if (emptyList) {
        console.log('empty list');
        emptyList.textContent = 'No hay eventos para mostrar';
    }
}

let addButtonsEventListeners = () => {
    let buttons = document.querySelectorAll('.fc-button.fc-button-primary');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            translateEmptyList();
        });
    });
}

// MAIN FUNCTION

document.addEventListener('DOMContentLoaded', function () {
    console.log(events);

    setupCalendar();
    disableToolbarButtons();
    addButtonsEventListeners();
});