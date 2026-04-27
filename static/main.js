//static/main.js
//document.getElementById('uploadForm').addEventListener('submit', async (e) => {
//e.preventDefault();
//const file = document.getElementById('file').files[0];
//if(!file){ alert('Choose file'); return; }
//const form = new FormData();
//form.append('file', file);
//form.append('camera_id', document.getElementById('camera_id').value || 'cam1');
//document.getElementById('status').innerText = "Processing completed. The vehicle number plate is extracted. Check Event Search.";
//const res = await fetch('/upload', { method:'POST', body: form });
//const j = await res.json();
//document.getElementById('status').innerText = JSON.stringify(j);
//});

document.getElementById('uploadForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const file = document.getElementById('file').files[0];
  if (!file) {
    alert('Choose file');
    return;
  }

  const form = new FormData();
  form.append('file', file);
  form.append('camera_id', document.getElementById('camera_id').value || 'cam1');

  document.getElementById('status').innerText = "Uploading and processing...";

  await fetch('/upload', { method: 'POST', body: form });

  // 🔁 POLL RESULT
  const interval = setInterval(async () => {
    const res = await fetch('/result');
    const data = await res.json();

    if (data.status === "completed") {
      document.getElementById('status').innerText =
        "Processing completed.\n" + data.message;
      clearInterval(interval);
    }
  }, 2000);
});


document.getElementById('searchBtn').addEventListener('click', async () => {
const plate = document.getElementById('plateQuery').value;
const q = plate ? `?plate=${encodeURIComponent(plate)}` : '';
const res = await fetch('/events/search' + q);
const arr = await res.json();
const table = document.getElementById('results');
table.innerHTML = '<tr><th>ID</th><th>ObjID</th><th>Plate</th><th>Camera</th><th>Location</th><th>Time</th></tr>';
arr.forEach(r=>{
const tr = document.createElement('tr');
tr.innerHTML = `<td>${r.id}</td><td>${r.object_id}</td><td>${r.plate||''}</td><td>${r.camera_id}</td><td>${r.location||''}</td><td>${r.timestamp}</td>`;
    table.appendChild(tr);
  });
});

document.getElementById('findLocBtn').addEventListener('click', async () => {
const plate = document.getElementById('locPlate').value;
if(!plate){ alert('Enter plate'); return; }
const res = await fetch(`/location?plate=${encodeURIComponent(plate)}`);
const j = await res.json();
const div = document.getElementById('locResult');
if(j.message){
div.innerText = j.message;
} else if(j.error){
div.innerText = j.error;
} else {
div.innerText = `Plate ${j.plate} last seen at ${j.location} (camera ${j.camera_id}) on ${j.last_seen}`;
}
});

document.getElementById('clearEventsBtn').addEventListener('click', async () => {
  if(!confirm("Delete all events?")) return;
  const res = await fetch('/events/clear', { method:'POST' });
  const j = await res.json();
  alert(j.status);
  document.getElementById('results').innerHTML = '';
});

