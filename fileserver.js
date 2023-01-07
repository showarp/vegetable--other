const express = require("express");
let app = express();
app.listen(3001);
app.use('/tempimage',express.static("C:\\Users\\Administrator\\Desktop\\webServer\\public\\tempimage"));
app.use('/dataimage',express.static("C:\\Users\\Administrator\\Desktop\\webServer\\public\\dataImage"));