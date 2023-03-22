
// EVENTS

let events = [
    {
    title: 'Pago 1',
    start: '2023-03-01',
    end: '2023-03-01'
    },
    {
    title: 'Pago 10',
    start: '2023-03-01',
    end: '2023-03-01'
    },
    {
    title: 'Pago 2',
    start: '2023-03-012',
    end: '2023-03-012'
    },
    {
    title: 'Pago 3',
    start: '2023-03-08',
    end: '2023-03-08'
    },
    {
    title: 'Pago 4',
    start: '2023-03-09',
    end: '2023-03-09'
    },
    {
    title: 'Pago 5',
    start: '2023-03-10',
    end: '2023-03-10'
    },
    {
    title: 'Pago 6',
    start: '2023-03-11',
    end: '2023-03-11'
    },
]


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
      click: function() {
        alert('clicked the custom button!');
      },
      disabled: true,
    },
    listButton: {
      icon: 'bi bi-list-ul',
      click: function() {
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
    });
    calendar.render();
}

let disableToolbarButtons = () => {
    let calendarButton = document.querySelector('.fc-calendarButton-button');
    let listButton = document.querySelector('.fc-listButton-button');

    calendarButton.disabled = true;
    listButton.disabled = true;
}


// MAIN FUNCTION

document.addEventListener('DOMContentLoaded', function() {
    setupCalendar();
    disableToolbarButtons();
});