const { execSync } = require('child_process');
const fs = require('fs');
const repo = 'C:\\Users\\getti\\Projects\\FUTURIA';
const token = fs.readFileSync('C:\\Users\\getti\\AppData\\Local\\Temp\\ghtoken.txt', 'utf8').replace(/[\r\n]/g, '').trim();
const auth = Buffer.from('diegogettig:' + token).toString('base64');
const header = 'Authorization: Basic ' + auth;
try {
  const out = execSync('git -c http.extraHeader="' + header + '" push origin main 2>&1', { cwd: repo, encoding: 'utf8', maxBuffer: 1024*1024*64 });
  console.log(out); console.log('PUSH OK');
} catch (e) {
  console.log('RESULT:', (e.stdout || '') + (e.stderr || '') || e.message); process.exit(1);
}