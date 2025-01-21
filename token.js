async function login(email, password) {
    let response = await fetch('/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });
    
    let data = await response.json();
    if (response.ok) {
        localStorage.setItem('jwt', data.access_token);
        alert('Inicio de sesión exitoso');
    } else {
        alert('Credenciales incorrectas');
    }
}

// Usar el token en una solicitud
async function cargarPreguntas() {
    let token = localStorage.getItem('jwt');
    let response = await fetch('/api/preguntas', {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    let preguntas = await response.json();
    console.log(preguntas);
}
