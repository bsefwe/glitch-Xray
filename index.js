const { execSync } = require("child_process");

execSync(`chmod +x ./start.sh && ./start.sh`,{
	cwd: './'
})
