# Trading backend compatibility source

Source: [Drakkar trading-backend](https://github.com/Drakkar-Software/trading-backend/tree/49434a30378e00127813dc1fcd6d671f4b69f575), version 1.2.43, commit `49434a30378e00127813dc1fcd6d671f4b69f575`. The original LGPL license and source copyright notices are retained. This source is vendored because the latest release and upstream HEAD import CCXT's removed private `static_dependencies.ecdsa` package, preventing OctoBot-Trading test collection with current CCXT.

The only runtime change imports the public `ecdsa.der` package directly and catches its `UnexpectedDER` exception. Packaging uses a `src` layout with explicit CCXT and ECDSA dependencies and the local version `1.2.43+ayu.1`. No upstream test cases are added to the consuming repository. Remove this compatibility source once upstream adopts the public ECDSA import.
