tannenbaum
==========
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/shashwatak/tannenbaum?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Design document

- API
  - /economy
    - GET /entity
    - GET /entity/:id
    - GET /entities/all
  - /index
    - GET /securities
    - GET /security/:id
    - GET /securities/all
  - /agent
    - POST /create
    - GET /portfolio
      "Authorized"
    - POST /buy/:securityID?min=:min
      "Authorized"
    - POST /sell/:securityID
      "Authorized"
    - GET /bids
      "Authorized"
  - Note: Authentication with OAuth
- Storage
  "Database tables"
  - securities
    - id
    - timestamp
    - price
  - entities
    - id
    - timestamp
    - value (points/second)
  - portfolio
    - id
    - balance
  - position
    - portfolioID
    - securityID
    - numShares
  - bid
    - portfolioID
    - securityID
    - type (buy/sell)
    - minValue
    - maxValue
    - timestamp
    - status (pending, executed, rejected)
- Classes
  - Server (Flask)
    - Serves API
  - Economy
    - Members
      - updateQueue
      - timeBetweenTicks (milliseconds)
      - lastTick (timestamp)
    - Functions
      - run()
        "Process"
        - Reads from persistent connection to data source
        - Adds to entities
      - getEntity(id)
      - updateEntity(id, dValue)
        - Creates entity if not exists
        - Updates its value
      - getEntities()
        - Returns: [id]
  - Index
    - Functions
      - run()
        "Process"
        - Read from entities
        - For entities that need tick
          - Update security
      - addBid(bid)
        - Adds to Storage (bid table)
      - updateSecurities()
        - Reads all pending bids and updates bids, securities
      - updateSecurity(id, value)
  - Agent
    - Class functions
      - create()
    - Functions
      - __init__(id, accessToken)
      - getPortfolio()
      - buy(securityID, numShares)
        - Returns: status (success, error)
      - sell(securityID, numShares)
        - Returns: status (success, error)
  - Security (DAO)
    - Functions
      - getLastPrice()
        - Returns: price
      - getWindow(period)
        - Returns: Window
  - Entity (DAO)
    - Functions
      - getCurrentValue()
        - Returns: value
  - Portfolio (DAO)
  - Position (DAO)
  - Bid (DAO)
  - Window (optional)
    - period (numTicks)
    - high
    - low
- Notes
  - Each tick is one buy/sell phase
    - Price goes up/down based on ratio between demand/supply
    - Change in price is a moving average over ticks (to smooth the fluctuation)
  - Can abstract away the buy/sell bidding, and just have everyone buy/sell to Bank
  - Need good simulations up front
    - So we can anticipate failure
  - How does the bank buy/sell in order to keep the market stable?
    - Will single-player mode have any risk?
      - Argument: No, because in a closed system, there's conservation of resources
        - You need multiple players
  - Is inflation healthy?
    - Argument: Yes, because value is being added and removed from the system constantly. Money needs to match that.