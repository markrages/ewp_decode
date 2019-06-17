# ewp_decode.py -- Decoding IAR .ewp project files

## What this is

This is a Python script to decode filenames out of the .ewp project files produced by IAR. This is useful when porting IAR projects to Makefiles.

I've done this kind of port several times. The ewp format is a reasonable XML format, but it is a bit too complicated for text-editor manipulation.  This rather simple helps out.

## What this is not

This does not write complete, working Makefiles. It only prints some defines in a make-compatible format.

It only looks for source files. It doesn't parse out pre- and post- build hooks, for example.

Send me a pull request if you extend the script in useful ways.

## Example usage

```Makefile

markrages@quitintime:~/src/ewp_decode$ ./ewp_decode.py /opt/nrf51sdk-10.0.0/examples/ble_central/experimental/ble_app_rscs_c/pca10028/ser_s120_spi/iar/ble_app_rscs_c_s120_spi_pca10028.ewp
NRF_SERIALIZATION_DIR := $(SRC_DIR)/../../../../../../../components/serialization
NRF_LIBRARIES_DIR := $(SRC_DIR)/../../../../../../../components/libraries
DOCUMENTATION_DIR := $(SRC_DIR)/../../..
NRF_DRIVERS_DIR := $(SRC_DIR)/../../../../../../../components
BOARD_SUPPORT_DIR := $(SRC_DIR)/../../../../../../bsp
APPLICATION_DIR := $(SRC_DIR)/../../..
NRF_BLE_DIR := $(SRC_DIR)/../../../../../../../components/ble
DEVICE_DIR := $(SRC_DIR)/../../../../../../../components/toolchain
NRF_SOFTDEVICE_DIR := $(SRC_DIR)/../../../../../../../components/softdevice
SOURCE_FILES += $(APPLICATION_DIR)/main.c
SOURCE_FILES += $(BOARD_SUPPORT_DIR)/bsp.c
SOURCE_FILES += $(BOARD_SUPPORT_DIR)/bsp_btn_ble.c
SOURCE_FILES += $(DEVICE_DIR)/system_nrf51.c
SOURCE_FILES += $(NRF_BLE_DIR)/ble_db_discovery/ble_db_discovery.c
SOURCE_FILES += $(NRF_BLE_DIR)/ble_services/ble_rscs_c/ble_rscs_c.c
SOURCE_FILES += $(NRF_BLE_DIR)/common/ble_advdata.c
SOURCE_FILES += $(NRF_BLE_DIR)/common/ble_srv_common.c
SOURCE_FILES += $(NRF_BLE_DIR)/device_manager/device_manager_central.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/ble_flash/ble_flash.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/common/nrf_drv_common.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/delay/nrf_delay.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/gpiote/nrf_drv_gpiote.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/nrf_soc_nosd/nrf_soc.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/pstorage/pstorage_nosd.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/spi_master/nrf_drv_spi.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/drivers_nrf/uart/nrf_drv_uart.c
SOURCE_FILES += $(NRF_DRIVERS_DIR)/libraries/uart/app_uart_fifo.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/button/app_button.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/fifo/app_fifo.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/mailbox/app_mailbox.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/scheduler/app_scheduler.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/timer/app_timer.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/trace/app_trace.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/uart/retarget.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/util/app_error.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/util/app_util_platform.c
SOURCE_FILES += $(NRF_LIBRARIES_DIR)/util/nrf_assert.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/middleware/app_mw_ble.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/middleware/app_mw_ble_gap.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/middleware/app_mw_ble_gattc.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/middleware/app_mw_ble_gatts.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/middleware/app_mw_ble_l2cap.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/middleware/app_mw_nrf_soc.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/app_ble_gap_sec_keys.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/app_ble_user_mem.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_enable.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_event.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_evt_tx_complete.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_evt_user_mem_release.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_evt_user_mem_request.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_address_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_address_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_adv_data_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_adv_start.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_adv_stop.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_appearance_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_appearance_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_auth_key_reply.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_authenticate.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_conn_param_update.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_conn_sec_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_connect.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_connect_cancel.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_device_name_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_device_name_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_disconnect.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_encrypt.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_adv_report.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_auth_key_request.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_auth_status.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_conn_param_update.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_conn_param_update_request.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_conn_sec_update.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_connected.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_disconnected.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_passkey_display.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_rssi_changed.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_scan_req_report.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_sec_info_request.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_sec_params_request.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_sec_request.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_evt_timeout.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_ppcp_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_ppcp_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_rssi_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_rssi_start.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_rssi_stop.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_scan_start.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_scan_stop.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_sec_info_reply.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_sec_params_reply.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gap_tx_power_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_char_value_by_uuid_read.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_char_values_read.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_characteristics_discover.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_descriptors_discover.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_char_disc_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_char_val_by_uuid_read_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_char_vals_read_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_desc_disc_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_hvx.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_prim_srvc_disc_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_read_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_rel_disc_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_timeout.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_evt_write_rsp.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_hv_confirm.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_primary_services_discover.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_read.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_relationships_discover.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gattc_write.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_characteristic_add.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_descriptor_add.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_evt_hvc.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_evt_rw_authorize_request.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_evt_sc_confirm.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_evt_sys_attr_missing.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_evt_timeout.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_evt_write.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_hvx.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_include_add.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_rw_authorize_reply.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_service_add.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_service_changed.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_sys_attr_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_sys_attr_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_value_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_gatts_value_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_l2cap_cid_register.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_l2cap_cid_unregister.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_l2cap_evt_rx.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_l2cap_tx.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_opt_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_opt_set.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_tx_buffer_count_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_user_mem_reply.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_uuid_decode.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_uuid_encode.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_uuid_vs_add.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/ble_version_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/power_system_off.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/codecs/s120/serializers/temp_get.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/hal/ser_app_hal_nrf51.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/hal/ser_app_power_system_off.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/transport/ser_sd_transport.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/application/transport/ser_softdevice_handler.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/ble_serialization.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/cond_field_serialization.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/struct_ser/s120/ble_gap_struct_serialization.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/struct_ser/s120/ble_gattc_struct_serialization.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/struct_ser/s120/ble_gatts_struct_serialization.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/struct_ser/s120/ble_struct_serialization.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/transport/ser_hal_transport.c
SOURCE_FILES += $(NRF_SERIALIZATION_DIR)/common/transport/ser_phy/ser_phy_nrf51_nrf_drv_spi.c
SOURCE_FILES += $(NRF_SOFTDEVICE_DIR)/common/softdevice_handler/softdevice_handler.c
```

Good luck!
Mark Rages
June 2019
