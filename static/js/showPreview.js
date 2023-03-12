const objectList = document.querySelectorAll('.object')

const dataElement = document.getElementById('data')
const objectName = document.getElementById('object-name').dataset.name


const objetos = JSON.parse(dataElement.dataset.json);


const preview = document.querySelector('#preview')
const prevInfo = document.querySelector('#prev-info')
const chevron = document.querySelector('#chevron')

objectList.forEach(object => {
  const moreInfo = object.querySelector('#moreInfo')
  object.addEventListener('click', () => {
    const isMobile = window.matchMedia("(max-width: 768px)").matches

    const isExpanded = !moreInfo.classList.contains('d-none')
    const objectId = object.querySelector('.object-id').innerText
    const objectData = objetos.find(object => object.id == objectId)


    if (isMobile) {
      if (isExpanded) {
        moreInfo.classList.add('d-none')
        chevron.classList.remove('bi-chevron-down')
        chevron.classList.add('bi-chevron-right')
      } else {
        moreInfo.classList.remove('d-none')
        chevron.classList.remove('bi-chevron-right')
        chevron.classList.add('bi-chevron-down')
      }

    } else {

      prevInfo.classList.add('d-none')
      preview.classList.remove('text-center')
      preview.classList.add('p-5')

      // add here the keys of the objects you want to show in the preview, translated to spanish 
      // do not remove the keys that are already there
      const config = {
        "title": "Título",
        "description": "Descripción",
        "amount": "Importe",
        "created_date": "Fecha",
        "donor_name": "Nombre",
        "donor_surname": "Apellidos",
        "donor_email": "Correo electrónico",
        "donor_dni": "DNI/CIF",
        "donor_address": "Dirección",

      }


      // this is the html that will be shown in the preview
      let html = ''
      for (let key in config) {
        if (Object.prototype.hasOwnProperty.call(objectData, key)) {
          if (key == 'title')
            html += `<h3>${config[key]}: ${objectData[key]}</h3>`
          else if (key == 'description')
            html += `<h5>${config[key]}: ${objectData[key] || "N/A"}</h5>`
          else if (key == 'amount')
            html += `<p>${config[key]}: ${objectData[key]} €</p>`
          else {
            html += `<p>${config[key]}: ${objectData[key]}</p>`
          }

        }

      }

      preview.innerHTML = `
          <div class="row">
            <div class="col-12">
              ${html}
            </div>
          </div>
        `
    }

  })

  // when resizing the window, the preview will be reset
  window.addEventListener('resize', () => {
    moreInfo.classList.add('d-none')
    prevInfo.classList.remove('d-none')
    preview.classList.add('text-center')
    preview.classList.remove('p-5')
    preview.innerHTML = `<span id="prev-info">Pulsa sobre una ${objectName} para la vista previa</span>`

  })

})
