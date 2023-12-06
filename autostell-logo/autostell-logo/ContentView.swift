//
//  ContentView.swift
//  autostell-logo
//
//  Created by MichealCodes  on 12/11/2023.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "suit.heart")
                .foregroundColor(.orange)
                .font(.system(size: 150))
                .imageScale(.large)
                .overlay(
                    VStack {
                        HStack {
                            Image(systemName: "gauge.open.with.lines.needle.67percent.and.arrowtriangle.and.car")
                                .foregroundColor(.orange)
                                .font(.system(size: 70))
                                .padding(-8)
                            Image(systemName: "gear")
                                .foregroundColor(.orange)
                                .font(.system(size: 70))
                                .padding(-8)
                            
                        }
                        .padding(-12)
                        Image(systemName: "person.3")
                            .foregroundColor(.orange)
                            .font(.system(size: 49))
                            .padding(-8)
                    }
                )
            Text("AUTOSTELL")
                .foregroundColor(.orange)
                .font(.system(size: 50))
                .fontWeight(/*@START_MENU_TOKEN@*/.bold/*@END_MENU_TOKEN@*/)
        }
    }
}

#Preview {
    ContentView()
}
