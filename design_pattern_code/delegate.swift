protocol HouseWorkDelegate {
  func startHouseWork()
  func cleanRoom()
  func makeDish()
  func finishHouseWork()
}


class Employer {
  var Servant:HouseWorkDelegate? = nil
  func doWork() {
      if let sv = self.Servant {
        sv.startHouseWork()
        sv.cleanRoom()
        sv.makeDish()
        sv.finishHouseWork()
      } else {
        print("今日は使用人がいないので家事をはじめます")
        print("掃除をします")
        print("料理を作ります")
        print("家事、終わります。自分で作る料理はうまくない")
      }
  }
}

class Servant : HouseWorkDelegate {
  func startHouseWork() {
    print("使用人が家事をはじめます")
  }
  func cleanRoom() {
    print("掃除をします")
  }
  func makeDish() {
    print("料理を作ります")
  }
  func finishHouseWork() {
    print("家事、終わります。美味しい料理ができました!")
  }
}

var employer = Employer()
var servant = Servant()

// 主人が家事をする
employer.doWork()

// 使用人が家事をする
employer.Servant = servant
employer.doWork()
