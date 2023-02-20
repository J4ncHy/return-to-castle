import express, { Express, Request, Response } from 'express';

const app: Express = express();
const port: number = 3000;

app.get("/", (req: Request, res: Response) => {

})

app.listen(port, () =>
    console.log('Example app listening on port 3000!'),
);