const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

export const apiUrl = isLocal
  ? 'http://localhost:8000/api/v1/' // Local Django server URL
  : 'https://evening-coast-93489-45f54e292976.herokuapp.com/api/v1/'; // Online Django server URL
