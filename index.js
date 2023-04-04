const { execSync } = require("child_process");

execSync(`chmod +x ./start.sh && ./start.sh`,{
	cwd: './',
	env: {
		id: `${process.env.id||'5aaed9b7-7fe3-47c3-bb52-db59859ce198'}`,
		PORT: `${process.env.PORT||8080}`
	}
})