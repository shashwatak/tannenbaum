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
    - tick
    - price
  - entities
    - id
    - timestamp
    - value (points/second)
  - agent
    - id
    - balance
  - portfolio
    - agentId
    - securityID
    - numShares
  - bid
    - type (buy/sell)
    - minValue
    - maxValue
    - timestamp
    - status (pending, executed, rejected)
- Classes
  - Economy
    - Members
      - updateQueue
    - Functions
      - updateValues()
        - Flushes queue, and updates storage
      - collect()
        - Opens persistent connection to data source, starts adding to queue
      - getEntity(id)
      - updateEntity(id, dValue)
        - Creates entity if not exists
        - Updates its value
      - getEntities()
        - Returns: [id]
  - Index
    - Functions
      - addBid(bid)
        - Adds to Storage (bid table)
      - updateSecurities()
        - Reads all pending bids and updates bids, securities
      - updateSecurity(id, value)
  - Agent (DAO)
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
  - Bid (DAO)
  - Portfolio (DAO)
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