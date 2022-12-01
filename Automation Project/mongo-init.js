db.createUser(
        {
            user: "amitvajpeyee",
            pwd: "amit1234",
            roles: [
                {
                    role: "readWrite",
                    db: "dap"
                }
            ]
        }
);