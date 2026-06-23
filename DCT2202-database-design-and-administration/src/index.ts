import pg, { ClientConfig, Notification } from "pg";

const config: ClientConfig = {
  user: process.env.PGUSER ?? "zauhdf",
  password: process.env.PGPASSWORD ?? "<DB_PASSWORD>",
  database: "postgres",
  host: "172.17.0.3",
  port: 5432,
};

const connectionString = `postgres://${config.user}:${config.password}@${config.host}:${config.port}/${config.database}`;

const pgClient = new pg.Client(connectionString);

pgClient.connect((err) => {
  if (err) {
    console.error("connection error", err.stack);
  } else {
    console.log("connected");
  }
});

// Call the listen
pgClient.query("LISTEN testevent");

// Setup a notification handler Listen
pgClient.on("notification", (message: Notification) => {
  const payload = JSON.parse(message.payload ?? "");
  console.log("payload::", payload);
});

// Insert a row in menssage
pgClient
  .query(
    `
  INSERT INTO
  message (id, content, sended_at, fk_user_id, fk_room_id)
  VALUES
  (12, 'Olá, tudo bem?', '2021-08-11', 1, 1)
`
  )
  .then((data) => {
    console.log("RESULT_QUERY_DATA", data);
  })
  .catch((err) => {
    console.log(err);
  });
