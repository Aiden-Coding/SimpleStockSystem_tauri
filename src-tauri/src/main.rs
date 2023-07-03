
// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

use std::process::Command;
fn main() {
    // Start the Python background thread
    //启动python后台
    let mut command = Command::new("python")
        .args(&["../run.py"])
        .spawn()
        .expect("Failed to start Python background thread");
        
        // todo 关闭时，同时关闭python后台
        // let mut command = Command::new("yes");
        // if let Ok(mut child) = command.spawn() {
        //     child.kill().expect("command wasn't running");
        // } else {
        //     println!("yes command didn't start");
        // }
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");

}
